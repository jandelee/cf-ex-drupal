"""Drupal Extension

Downloads, installs and configures Drupal
"""
import os
import os.path
import logging
from build_pack_utils import utils


_log = logging.getLogger('drupal')


DEFAULTS = utils.FormattedDict({
    'DRUPAL_VERSION': '8.5.9',
    'DRUPAL_PACKAGE': 'drupal-{DRUPAL_VERSION}.tar.gz',
    'DRUPAL_HASH': ''3db4ab3674ae38d1b15d5faac3b10ff0,
    'DRUPAL_URL': 'http://ftp.drupal.org/files/projects/{DRUPAL_PACKAGE}'
})


# Extension Methods
def preprocess_commands(ctx):
    return ()


def service_commands(ctx):
    return {}


def service_environment(ctx):
    return {}


def compile(install):
    print 'Installing Drupal %s' % DEFAULTS['DRUPAL_VERSION']
    ctx = install.builder._ctx
    inst = install._installer
    workDir = os.path.join(ctx['TMPDIR'], 'drupal')
    inst.install_binary_direct(
        DEFAULTS['DRUPAL_URL'],
        DEFAULTS['DRUPAL_HASH'],
        workDir,
        fileName=DEFAULTS['DRUPAL_PACKAGE'],
        strip=True)
    (install.builder
        .move()
        .everything()
        .under('{BUILD_DIR}/htdocs')
        .into(workDir)
        .done())
    (install.builder
        .move()
        .everything()
        .under(workDir)
        .into('{BUILD_DIR}/htdocs')
        .done())
    return 0
