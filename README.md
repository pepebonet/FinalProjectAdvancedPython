# FinalProjectAdvancedPython
This is my final project for advanced python

## Nesting clicks

If you look at the `sample_script.py` you have an example of nesting click. You have a group and then the other two click.commands that now are nested because we are getting the group and using cli (See lines 7 and 15).

To call this script we can do:

    python scripts/sample_script.py say-name -pn Manolo
    python scripts/sample_script.py say-age -pa 20

As a reference you can check more examples [here](https://stackoverflow.com/questions/34643620/how-can-i-split-my-click-commands-each-with-a-set-of-sub-commands-into-multipl) or in the [click documentation](https://click.palletsprojects.com/en/8.1.x/commands/)