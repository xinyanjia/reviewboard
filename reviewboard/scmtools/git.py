    supports_authentication = True
        super(GitTool, self).__init__(repository)

        local_site_name = None

        if repository.local_site:
            local_site_name = repository.local_site.name

        self.client = GitClient(repository.path, repository.raw_file_url,
                                repository.username, repository.password,
                                local_site_name)
    def check_repository(cls, path, username=None, password=None,
                         local_site_name=None):
        client = GitClient(path, local_site_name=local_site_name)
        super(GitTool, cls).check_repository(client.path, username, password,
                                             local_site_name)
    def __init__(self, path, raw_file_url=None, username=None, password=None,
                 local_site_name=None):
        self.username = username
        self.password = password
        self.local_site_name = local_site_name
    def _get_file(self, url):
        host = urlparse.urlparse(url)[1]
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, host, self.username, self.password)
        auth_handler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(auth_handler)
        f = opener.open(url)
        return f.read()

                return self._get_file(url)
                return self._get_file(url)
        return SCMTool.popen(['git'] + args,
                             local_site_name=self.local_site_name)
            return 'ssh://%s%s%s' % (m.group('username') or '',