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
all_index = {'name': 'description',
             'name': 'description'}

# Top ten popular add-ons
popular_index = {'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description',
                 'name': 'description'}

# By JK (Jackkillian) index
by_jk_index = {'name': 'description',
               'name': 'description'}

# File Types index
file_types_index = {'name': 'description',
                    'name': 'description'}

# Programming languges index
programming_index = {'name': 'description',
                     'name': 'description'}
