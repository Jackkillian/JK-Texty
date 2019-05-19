"""
Name:      JK Texty - Store - Code - index.py
Version:   1.0.0
Author:    @Jackkillian
License:   MIT License
========
JK Texty Store
===
This file and others are downloaded by Texty. That is how Texty knows what is in the store.
Each index contains a name and a description.
"""
# Store status (if not good, Texty will give an error and not open the store)
# Statuses: 'True' (up and running) 'False' (error) 'Empty' (empty store) 'Discontinued' (the store is discontinued)
store_status = 'True'

# Description for 'False' store status
false_description = 'There is nothing wrong with the store'

# Description for 'Discontinued' store status
discontinued_description = 'The store is not discontinued'

# List of indexes
index_list = {'all_index': 'All Add-Ons',
              'popular_index': 'Top Ten Add-Ons',
              'by_jk_index': 'Add-Ons by JK',
              'file_types_index': 'Add-Ons for saving files for other programs',
              'programming_index': 'Add-Ons for programming language IDEs'}

# All index
all_index = {'all1': 'description',
             'Jack\'s_Extension': 'description'}

# Top ten popular add-ons
popular_index = {'popular1': 'description',
                 'popular2': 'description',
                 'popular3': 'description',
                 'popular4': 'description',
                 'popular5': 'description',
                 'popular6': 'description',
                 'popular7': 'description',
                 'popular8': 'description',
                 'popular9': 'description',
                 'popular10': 'description'}

# By JK (Jackkillian) index
by_jk_index = {'by_jk1': 'description',
               'by_jk2': 'description'}

# File Types index
file_types_index = {'file_types1': 'description',
                    'file_types2': 'description'}

# Programming languges index
programming_index = {'programming1': 'description',
                     'programming2': 'description'}
