#
# Copyright 2014-2017 AT&T Intellectual Property
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from heatclient import client
from keystoneauth1 import loading
from keystoneauth1 import session
from oslo_config import cfg

VERSION = 1

CONF = cfg.CONF


class Heat(object):

    def __init__(self, _logger):
        self.logger = _logger
        self.heat = None

    def _set_heat_client(self):
        '''Set connection to Heat API.'''

        loader = loading.get_plugin_loader('password')
        auth = loader.load_from_options(
            auth_url=CONF.identity.auth_url,
            username=CONF.identity.username,
            password=CONF.identity.password,
            project_name=CONF.identity.project_name)

        sess = session.Session(auth=auth)
        self.heat = client.Client('1', session=sess)

    def get_stacks(self):
        '''Return stacks, each of which is a JSON dict.'''

        # collecting and formating to JSON dict.

        # return stacks
        pass
