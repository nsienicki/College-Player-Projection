import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import pairwise_distances, euclidean_distances
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import KElbowVisualizer
from collections import defaultdict

###################################
######## Data Input ###############
###################################

# read in data
players_df_edited = pd.read_csv('data/player_data_college_2010-2025.csv')



# apply filters
players_df_edited.dropna(inplace=True)

only_NBA = True
if only_NBA:
    nba_map = pd.read_csv('data/nba_ncaa_map.csv')
    players_df_edited = players_df_edited[players_df_edited['ncaa_id'].isin(nba_map['ncaa_id'])]

# remove more columns for model processing
model_columns_to_drop = ['player_name', 'team', 'min_year', 'max_year', 'pos_class', 'type', 'avg_pick', 'ncaa_id']
players_df_model = players_df_edited.drop(
    columns=[col for col in model_columns_to_drop if col in players_df_edited.columns])


# clean data (remove NaN)


###################################
######## Feature Selection ########
###################################

# standardize data
scaler = StandardScaler()
scaler_players_df = scaler.fit_transform(players_df_model)



def principal_component_selection(X, n_clusters=None, n_components=10):
    # feature selection kmeans based on PCA, structure from
    # https://datascience.stackexchange.com/questions/67040/how-to-do-feature-selection-for-clustering-and-implement-it
    # -in-python
    pca = PCA(n_components=n_components).fit(X)
    A_q = pca.components_.T

    if n_clusters == None:
        kmeans = KMeans(n_init='auto').fit(A_q)
    else:
        kmeans = KMeans(n_clusters=n_clusters, n_init='auto').fit(A_q)
    clusters = kmeans.predict(A_q)
    cluster_centers = kmeans.cluster_centers_

    dists = defaultdict(list)
    for i, c in enumerate(clusters):
        dist = euclidean_distances([A_q[i, :]], [cluster_centers[c, :]])[0][0]
        dists[c].append((i, dist))

    # gives inds of selected features based on variance
    pfa_indices = [sorted(f, key=lambda x: x[1])[0][0] for f in dists.values()]

    return pfa_indices


# pfa feature selected model input
pfa_inds_23_24 = principal_component_selection(scaler_players_df)
pfa_players_df = players_df_model.iloc[:, pfa_inds_23_24]
print(pfa_players_df.columns)

# hand selected model input; advanced shooting data only
hand_selected_vars = ['avg_offensive_rebound_pct', 'avg_defensive_rebound_pct', 'avg_2p_made']
hand_players_df = players_df_model[hand_selected_vars]


###################################
######## Feature Evaluation #######
###################################

# big loop to compare cluster difference scores
def run_k_selection_and_record_scores(datasets, k_range=(2, 11)):
    results = []

    for dataset_name, data in datasets.items():
        print(f"Processing dataset: {dataset_name}")

        # Initialize KMeans and KElbowVisualizer
        model = KMeans(random_state=1, n_init='auto')
        visualizer = KElbowVisualizer(model, k=k_range, metric='calinski_harabasz', timings=False, locate_elbow=True)

        # Fit the visualizer to the data
        visualizer.fit(data)
        visualizer.show()
        # Record silhouette scores
        for k, score in zip(range(k_range[0], k_range[1] + 1), visualizer.k_scores_):
            results.append({'Dataset': dataset_name, 'K': k, 'CH Index': score})

    # Convert results to a DataFrame
    results_df = pd.DataFrame(results)
    return results_df


# list of datasets to compare
datasets = {
    'pfa_players_df': StandardScaler().fit_transform(pfa_players_df),
    #'hand_players_df': StandardScaler().fit_transform(hand_players_df),
    'players_df_model': StandardScaler().fit_transform(players_df_model),
}

# execute
k_range = (3, 15)
results_df = run_k_selection_and_record_scores(datasets, k_range=k_range)
best_CH_row = best_row = results_df.loc[results_df["CH Index"].idxmax()]
best_dataset = best_row["Dataset"]
best_dataset_obj = datasets[best_dataset]
best_k = best_row["K"]
results_df.to_csv('eval_scores.csv', index=False)
plt.close()

####################################
# Final KMeans Implementation ######
####################################

# run KMeans
kmeans_model_23_24 = KMeans(random_state=1, n_init='auto', n_clusters=best_k)
kmeans_model_23_24.fit(best_dataset_obj)

# predict
players_df_edited['cluster'] = kmeans_model_23_24.predict(best_dataset_obj)
players_df_edited.to_csv('player_cluster.csv', index=False)

####################################
########### PCA and graph ##########
####################################
pca = PCA(n_components=2)
pca = pca.fit_transform(best_dataset_obj)

pca_df = pd.DataFrame(pca, columns=['PC1', 'PC2'])

# plot the first two principal components, include cluster labels
plt.figure(figsize=(8, 6))
plt.scatter(pca_df['PC1'], pca_df['PC2'], alpha=0.7, c=players_df_edited['cluster'], cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Player Clusters')
plt.colorbar()
plt.savefig('pca_cluster.png')
plt.show()
players_df_edited['PC1'] = pca_df['PC1']
players_df_edited['PC2'] = pca_df['PC2']
players_df_edited.to_csv('player_cluster.csv', index=False)

####################################
####### Positional Purity ##########
####################################
# find positional mode of each cluster
positional_purity = True
if positional_purity:
    def positional_purity(player_df):
        position_stats = (
            player_df.groupby('cluster')['pos_class'].apply(lambda x: x.mode()[0]).reset_index(
                name='most_likely_position')
        )
        # find percentage of the mode position in each cluster
        position_percentage = (
            player_df.groupby('cluster')['pos_class']
            .apply(lambda x: (x == x.mode()[0]).mean() * 100)  # percentage of mode position in each cluster
            .reset_index(name='position_percentage')
        )
        # merge the position stats and percentage
        cluster_position_info = pd.merge(position_stats, position_percentage, on='cluster')

        return cluster_position_info



    clusters_df = positional_purity(players_df_edited)
    clusters_df.to_csv('cluster_stats.csv', index=False)
