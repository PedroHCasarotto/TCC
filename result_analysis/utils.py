
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from typing import Tuple
import warnings
warnings.filterwarnings('ignore')

existing_molecules = []

MACRO_PATH = '../TransGEM-main'
TOTAL_MOLECULES_GENERATED = 3000

def set_up_and_print_metrics(dataset: str='binary', precision_points: int=3) -> Tuple[pd.DataFrame, pd.DataFrame]:

    path_normal = f'{MACRO_PATH}/result/df_fame_test/decimal_points_{precision_points}/{dataset}/_maxint_10_genelength978_dim64_n6h8ff512_bh4_lr0.0001.csv'
    path_changed = f'{MACRO_PATH}/result/df_fame_cl_test/decimal_points_{precision_points}/{dataset}/_maxint_0_genelength64_dim64_n6h8ff512_bh4_lr0.0001.csv'

    df_original = pd.read_csv(path_normal)
    df_altered = pd.read_csv(path_changed)

    test_samples = pd.read_csv(f'{MACRO_PATH}/data/df_fame_test.csv')

    df_original['substance'] = test_samples.pert_iname
    df_altered['substance'] = test_samples.pert_iname

    map_substance = {
        'dexamethasone': 'Dexametasona',
        'testosterone': 'Testosterona'
    }

    df_original['substance'] = df_original['substance'].apply(lambda x: map_substance[x])
    df_altered['substance'] = df_altered['substance'].apply(lambda x: map_substance[x])


    # TOTAL_MOLECULES_GENERATED molecules are generated, but some of the are repeted
    df_original['n'] = df_original.unique.apply(lambda x: int(x*TOTAL_MOLECULES_GENERATED))
    df_altered['n'] = df_altered.unique.apply(lambda x: int(x*TOTAL_MOLECULES_GENERATED))

    if (df_original.valid.mean() != 1):
        raise KeyError

    return df_original, df_altered

def get_generated_molecules(l: list) -> list:
    '''Get each generated molecule'''
    columns = l.str.slice(1, -1).str.replace('"', '').str.split("', '")
    for column in columns:
        column[0] = column[0][1:]
    return columns

def compare(list_molecules: list, existing_molecules: list) -> list:
    '''Compare each generated molecule and see if it aleady exists in train and test molecules set'''
    results = []
    for list_m in list_molecules:
        count_sucess = 0
        for item in list_m:
            if item in existing_molecules:
                count_sucess = count_sucess + 1
        results.append(1 - count_sucess/len(list_m))
    
    return results

def generate_novelty(df_original, df_altered) -> Tuple[pd.DataFrame, pd.DataFrame]:
    '''Add novelty metics in validation dataset.'''
    list_molecules = get_generated_molecules(df_original.preds)
    novelty_original = compare(list_molecules, existing_molecules)
    df_original['novelty'] = pd.Series(novelty_original)

    list_molecules = get_generated_molecules(df_altered.preds)
    novelty_altered = compare(list_molecules, existing_molecules)
    df_altered['novelty'] = pd.Series(novelty_altered)

    return df_original, df_altered


def plot_info_model_filter_original(df_original: pd.DataFrame, df_altered: pd.DataFrame, dataset:str, column: str, type='boxplot') -> None:
    '''Plots distribution of metrics to each validation sample'''

    df_original['GED'] = 'Não'
    df_altered['GED'] = 'Sim'

    df_combined = pd.concat([df_original[df_original['substance'] == 'dexamethasone'], 
                             df_altered[df_altered['substance'] == 'dexamethasone']])
    df_combined['Subset'] = 'dexamethasone'

    df_combined_2 = pd.concat([df_original[df_original['substance'] == 'testosterone'], 
                               df_altered[df_altered['substance'] == 'testosterone']])
    df_combined_2['Subset'] = 'testosterone'

    df_final = pd.concat([df_combined, df_combined_2])

    g = sns.FacetGrid(df_final, col="Subset", sharey=True, height=4, aspect=1.2)
    if (type == 'violine'):
        g.map(sns.violinplot, "GED", column, palette="Set3")
    elif (type == 'boxplot'):
        g.map(sns.boxplot, "GED", column, palette="Set3")

    g.set_titles("{col_name}")
    plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
    g.set_axis_labels("GED", column.title())
    
    plt.suptitle(f"Dataset {dataset.title()}: Box Plots for {column.title()} Across Substances", y=1.02, fontsize=16)
    plt.tight_layout()
    plt.show()

def plot_info_model_filter(df_original: pd.DataFrame, df_altered: pd.DataFrame, dataset: str, column: str, type: str='boxplot', dodge_spacing: bool=True, box_width:float=0.6, figsize: tuple=(10, 6)) -> None:
    '''Plots distribution of metrics to each validation sample'''

    # Adding 'GED' column
    df_original['GED'] = 'Não'
    df_altered['GED'] = 'Sim'

    metrics_map = {
        'unique': 'Unicidade',
        'div': 'Diversidade Interna',
        'qed_mid': 'QED Médio'
    }

    # Combining subsets for both substances
    df_combined = pd.concat([df_original, df_altered])
    df_combined = df_combined[df_combined['substance'].isin(['Dexametasona', 'Testosterona'])]
    
    # Creating the plot
    plt.figure(figsize=figsize)
    
    if type == 'violine':
        sns.violinplot(
            data=df_combined, x="GED", y=column, hue="substance", 
            palette="Set2", split=dodge_spacing
        )
    elif type == 'boxplot':
        sns.boxplot(
            data=df_combined, x="GED", y=column, hue="substance", 
            palette="Set2", dodge=dodge_spacing, width=box_width
        )

    # Adding grid
    plt.grid(visible=True, which='major', axis='y', linestyle='--', linewidth=0.8, alpha=0.7)
    plt.minorticks_on()  # Enable minor ticks
    plt.grid(visible=True, which='minor', axis='y', linestyle=':', linewidth=0.5, alpha=0.5)

    # Legend, title, and layout
    plt.legend(title='Substância', loc='lower left')
    plt.tight_layout()

    plt.ylabel(metrics_map[column])
    plt.xlabel('GED')
    # Show plot
    plt.show()

def plot_info_model_filter_swapped(df_original: pd.DataFrame, df_altered: pd.DataFrame, dataset: str, column: str, type='boxplot', legend_loc: int=0, dodge_spacing=True, box_width=0.6, figsize=(10, 6)) -> None:
    '''Plots distribution of metrics to each validation sample, swapped'''
    
    # Adding 'GED' column
    df_original['GED'] = 'Não'
    df_altered['GED'] = 'Sim'

    metrics_map = {
        'unique': 'Unicidade',
        'div': 'Diversidade Interna',
        'qed_mid': 'QED Médio'
    }

    # Combining subsets for both substances
    df_combined = pd.concat([df_original, df_altered]).reset_index()
    df_combined = df_combined[df_combined['substance'].isin(['Dexametasona', 'Testosterona'])]
    
    # Creating the plot
    plt.figure(figsize=figsize) 
    
    if type == 'violine':
        sns.violinplot(
            data=df_combined, x="substance", y=column, hue="GED", 
            palette="tab10", split=dodge_spacing
        )
    elif type == 'boxplot':
        sns.boxplot(
            data=df_combined, x="substance", y=column, hue="GED", 
            palette="tab10", dodge=dodge_spacing, width=box_width
        )

    # Adding grid
    plt.grid(visible=True, which='major', axis='y', linestyle='--', linewidth=0.8, alpha=0.7)
    plt.minorticks_on()  # Enable minor ticks
    plt.grid(visible=True, which='minor', axis='y', linestyle=':', linewidth=0.5, alpha=0.5)

    # Legend, title, and layout
    plt.legend(title='GED', loc=legend_loc, fontsize=12)
    plt.tight_layout()

    plt.ylabel(metrics_map[column])
    plt.xlabel('Substância')
    # Show plot
    plt.show()


def print_results_model(df_original: pd.DataFrame, df_altered: pd.DataFrame, col: str) -> None:
    '''Prints mean and stendart desviation to each smaple.'''
    print(f'For {col} column:')
    print(f'For original model: {df_original[col].mean():.2f}, {df_original[col].std():.2f}')
    print(f'For altered model: {df_altered[col].mean():.2f}, {df_altered[col].std():.2f}')
    print("\n")


def print_results_model_with_substance_analysis(df_original: pd.DataFrame, df_altered: pd.DataFrame, col: str):
    '''Return prints about substane analysis.'''
    print(f'For {col} column:')
    print(f'For original model:')
    print(f"{df_original.groupby('substance')[col].mean().index[0]}: {df_original.groupby('substance')[col].mean()[0]:.2f} +- {df_original.groupby('substance')[col].std()[0]:.2f}%, mediana de {df_original.groupby('substance')[col].median()[0]:.2f}")
    print(f"{df_original.groupby('substance')[col].mean().index[1]}: {df_original.groupby('substance')[col].mean()[1]:.2f} +- {df_original.groupby('substance')[col].std()[1]:.2f}%, mediana de {df_original.groupby('substance')[col].median()[1]:.2f}")
    print(f'For altered model:')
    print(f"{df_altered.groupby('substance')[col].mean().index[0]}: {df_altered.groupby('substance')[col].mean()[0]:.2f} +- {df_altered.groupby('substance')[col].std()[0]:.2f}%, mediana de {df_altered.groupby('substance')[col].median()[0]:.2f}")
    print(f"{df_altered.groupby('substance')[col].mean().index[1]}: {df_altered.groupby('substance')[col].mean()[1]:.2f} +- {df_altered.groupby('substance')[col].std()[1]:.2f}%, mediana de {df_altered.groupby('substance')[col].median()[1]:.2f}")
    print("\n")
