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
all_index = {'AppleScript': 'Write AppleScript programes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
             'C': 'Write C programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
             'C++': 'Write C++ programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
             'HTML': 'Write HTML programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
             'JK_Dashboard_Extension': 'Write JK Dashboard Extensions with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and JK Dashboard Making documentation.',
             'JK_PyApp': 'Write JK PyApps with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and Making JK PyApp documentation.',
             'JavaScript': 'Write JavaScript programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
             'Markdown': 'Write Markdown files with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and a Markdown file previewer.',
             'Python': 'Write Python programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
             'Python_GUI_App': 'Write Python GUI Apps with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and Python GUI App documentation.',
             'Plain_Text': 'Write Plain Text files with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.',
             'Rich_Text': 'Write Rich Text fils with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures font and color options.',
             'Ruby': 'Write Ruby programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.'}

# Top ten popular add-ons
popular_index = {'AppleScript': 'Write AppleScript programes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
                 'HTML': 'Write HTML programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
                 'JK_Dashboard_Extension': 'Write JK Dashboard Extensions with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and JK Dashboard Making documentation.',
                 'JK_PyApp': 'Write JK PyApps with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and Making JK PyApp documentation.',
                 'JavaScript': 'Write JavaScript programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
                 'Markdown': 'Write Markdown files with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and a Markdown file previewer.',
                 'Python': 'Write Python programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
                 'Python_GUI_App': 'Write Python GUI Apps with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and Python GUI App documentation.',
                 'Plain_Text': 'Write Plain Text files with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.',
                 'Rich_Text': 'Write Rich Text fils with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures font and color options.'}

# By JK (Jackkillian) index
by_jk_index = {'AppleScript': 'Write AppleScript programes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
               'C': 'Write C programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
               'C++': 'Write C++ programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
               'HTML': 'Write HTML programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
               'JK_Dashboard_Extension': 'Write JK Dashboard Extensions with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and JK Dashboard Making documentation.',
               'JK_PyApp': 'Write JK PyApps with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and Making JK PyApp documentation.',
               'JavaScript': 'Write JavaScript programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
               'Markdown': 'Write Markdown files with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and a Markdown file previewer.',
               'Python': 'Write Python programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
               'Python_GUI_App': 'Write Python GUI Apps with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and Python GUI App documentation.',
               'Plain_Text': 'Write Plain Text files with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.',
               'Rich_Text': 'Write Rich Text fils with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures font and color options.',
               'Ruby': 'Write Ruby programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.'}

# File Types index
file_types_index = {'None' : 'There are no file type add-ons yet.'}
"""
file_types_index = {'file_types1': 'description',
                    'file_types2': 'description'}
"""

# Programming languges index
programming_index = {'AppleScript': 'Write AppleScript programes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
                     'C': 'Write C programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
                     'C++': 'Write C++ programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
                     'HTML': 'Write HTML programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
                     'JK_Dashboard_Extension': 'Write JK Dashboard Extensions with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and JK Dashboard Making documentation.',
                     'JK_PyApp': 'Write JK PyApps with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and Making JK PyApp documentation.',
                     'JavaScript': 'Write JavaScript programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
                     'Markdown': 'Write Markdown files with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and a Markdown file previewer.',
                     'Python': 'Write Python programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.',
                     'Python_GUI_App': 'Write Python GUI Apps with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting and Python GUI App documentation.',
                     'Plain_Text': 'Write Plain Text files with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.',
                     'Rich_Text': 'Write Rich Text fils with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures font and color options.',
                     'Ruby': 'Write Ruby programmes with this add-on! It should be built-in, but if it isn\'t,\nyou can install it here.\nFeatures basic syntax highlighting.'}
