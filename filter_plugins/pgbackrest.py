

def repositories_path(repositories_list):
    """
    Returns a list of paths in the options of repositories.
    """
    return [option['value'] for repository in repositories_list for option
            in repository['options'] if option['name'] == 'path']


def spool_path(options_list):
    """
    Returns the spool path from the options list.
    """
    return [option['value'] for option
            in options_list if option['name'] == 'spool-path']


class FilterModule(object):

    def filters(self):
        return {
            'repositories_path': repositories_path,
            'spool_path': spool_path
        }
