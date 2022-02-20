import pandas as pd
from typing import List, Dict, Tuple
from numpy import array, empty, zeros

def _determine_distances(pair_1: str, pair_2: str, pairs_df: pd.DataFrame, min_cM: int) -> None:
    """Function that will determine the distances between the main grid and then each connected grid. It will use a value of 2.5 for all grids that don't share a segment. This is just the min cM value, 5cM, divided in half

    Parameter:
    __________
    pair_1 : str
        string that has the main grid id
    
    
    pairs_df : pd.DataFrame
        dataframe from the pairs file that has been filtered to just connections with the main grid
    """
    if pair_2 == pair_1:

        return float(0)

    # pulling out the length of the IBD segment based on hapibd
    filtered_pairs:pd.DataFrame = pairs_df[((pairs_df["pair_1"] == pair_1) & (pairs_df["pair_2"] == pair_2)) | ((pairs_df["pair_1"] == pair_2) & (pairs_df["pair_2"] == pair_1))]

    if filtered_pairs.empty:

        ibd_length: float = min_cM/2

        print(f"no pairwise sharing for grids {pair_1} and {pair_2}. Using an ibd length of {ibd_length}cM instead")    
    
    else:
        ibd_length: float = filtered_pairs["length"].values.tolist()[0] 

    return 1/ibd_length


def record_matrix(output: str, matrix: array, pair_list: List[str]) -> None:
    """Function that will write the dataframe to a file
    
    Parameters
    
    output : str
        filepath to write the output to
    
    matrix : array
        array that has the distance matrix for each individual
    
    pair_list : List[str]
        list of ids that represent each row of the pair_list
    """

    with open(output, "w") as output_file:
        for i in range(len(pair_list)):
            distance_str = '\t'.join([str(distance) for distance in matrix[i]])
            output_file.write(f"{pair_list[i]}\t{distance_str}\n")
            

def make_distance_matrix(pairs_df: pd.DataFrame, min_cM: int) -> Tuple[List[str], array]:
    """Function that will make the distance matrix
    
    Parameters
    
    pairs_df : pd.DataFrame
        dataframe that has the pairs_files. it should have at least three columns 
        called 'pair_1', 'pair_2', and 'length'

    min_cM : float
        This is the minimum centimorgan threshold that will be divided in half to 
        get the ibd segment length when pairs do not share a segment

    Returns

    Dict[str, Dict[str, float]]
        returns a tuple where the first object is a list of ids that has the 
        individual id that corresponds to each row. The second object is the 
        distance matrix
    """
    # get a list of all the unique ids in the pairs_df
    id_list: List[str] = list(set(pairs_df.pair_1.values.tolist()+pairs_df.pair_2.values.tolist()))
    
    matrix: array = zeros((len(id_list), len(id_list)), dtype= float)

    ids_index = []

    for i in range(len(id_list)):
        
        ids_index.append(id_list[i])

        for j in range(len(id_list)):
            
            distance = _determine_distances(id_list[i], id_list[j], pairs_df, min_cM)

            matrix[i][j] = distance

    return ids_index, matrix

    

