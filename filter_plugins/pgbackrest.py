

def repositories_path(repositories_list):
    """
    Returns a list of paths in the options of repositories.
    """
    return [option['value'] for repository in repositories_list for option
            in repository['options'] if option['name'] == 'path']


class FilterModule(object):

    def filters(self):
        return {
            'repositories_path': repositories_path
        }
