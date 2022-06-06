import numpy as np
import pandas as pd
from datetime import datetime


######################################################################################################


                ####################
                #                  #
                # LOAD EXPORT MENU #
                #                  #
                ####################


def load_export_menu(dataset):

    print()
    print("         ##########################")
    print("         ##                      ##")
    print("         ##  LOAD - EXPORT MENU  ##")
    print("         ##                      ##")
    print("         ##########################")


    exit_variable=0

    while exit_variable==0:
        print()
        print("What would you like to do :")
        print()
        print("1) Load a datset.")
        print("2) Export a datset.")
        print("0) Return to Main Menu.")
        load_export_choice=input("Enter your choice: ")

        if load_export_choice=="1":
            continue_load=input("Remember to export your datset before loading a new one, would you like to proceed with the loading (y/n)? ")
            if continue_load=="y":
                dataset=load_dataset(int(load_export_choice)).copy()

        elif load_export_choice=="2":
            export_dataset(dataset)

        elif load_export_choice=="0":
            exit_variable=1

        else:
            print()
            print("Please enter a valid choice.")

    return dataset


######################################################################################################


                #########################
                #                       #
                # LOAD DATASET FUNCTION #
                #                       #
                #########################


def load_dataset (message_indicator):

    if message_indicator==0:
        print()
        print("Since there is no dataset loaded, the export option is not avaliable.")
    print()
    print("To load a datset please answer the following questions.")
    extension=input("Enter the extension of your dataset (csv, xlsx): ")
    name_file=input("Enter the name of your file (without extension): ")
    if extension=="csv":
        name_file=name_file + ".csv"
        separ=input("Enter the separation symbol of your data: ")
        df_to_clean = pd.read_csv(name_file, sep=separ)

    elif extension=="xlsx":
        name_file=name_file + ".xlsx"
        name_sheet=input("Enter the name of the sheet: ")
        df_to_clean = pd.read_excel(name_file, sheet_name=name_sheet)

    else:
        print()
        print("The extension", extension, "is not supported.")
        print()

        no_data_loaded = {'Error_message': ['No dataset loaded']}
        df_to_clean = pd.DataFrame(no_data_loaded)

        print("No dataset was loaded")

        return df_to_clean


    print()
    print("The dataset has been loaded.")

    return df_to_clean


######################################################################################################


                ###########################
                #                         #
                # EXPORT DATASET FUNCTION #
                #                         #
                ###########################


def export_dataset (df_to_export):

    print()
    extension_file=input("Enter the extension you would like to use to export the set (csv, xlsx): ")
    if extension_file=="csv":
        name_export_file=input("Enter the name for the new file: ")
        name_export_file=name_export_file + ".csv"
        df_to_export.to_csv(name_export_file, index = False)

    elif extension_file=="xlsx":
        name_export_file=input("Enter the name for the new file: ")
        name_export_file=name_export_file + ".xlsx"
        df_to_export.to_excel(name_export_file, index = False)

    print()
    print("The dataset was exported.")

    return ()


######################################################################################################


while running_variable!=0:
    print()
    print("         #################")
    print("         ##             ##")
    print("         ##  MAIN MENU  ##")
    print("         ##             ##")
    print("         #################")

    print()
    print("What would you like to do :")
    print()
    print("1) Load or export a datset.")
    print("2) Display basic information of the dataset.")
    print("3) Display lines of the dataset.")
    print("4) Change the type of a column.")
    print("5) Fix encoding errors in a column ('Ä' appears as 'Ã„').")
    print("6) Take care of missing data.")
    print("7) Modify data.")
    print("8) Select relevant data.")
    print("0) Exit.")
    print()
    choose_desire=input("Enter your choice: ")

    if choose_desire=="1":
        if dataset_iterated!=0:
            df_to_work=load_export_menu(df_to_work).copy()

        else:
            df_to_work=load_dataset(dataset_iterated).copy()
            dataset_iterated=1

        if df_to_work.columns[0]=='Error_message':
            dataset_iterated=0




    elif choose_desire=="0":
        continue_exit=input("Remember to export your datset, any change made before the last export wont be saved. Do you want to exit (y/n)? ")
        if continue_exit=="y":
            running_variable=0

    else:
        print()
        print("Please enter a valid choice.")
