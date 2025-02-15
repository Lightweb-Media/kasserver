# kasserver - Manage domains hosted on All-Inkl.com through the KAS server API
# Copyright (c) 2018 Christian Fetzer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Manage DNS records for All-Inkl.com domains through the KAS server"""

import logging

import click

import kasserver

LOGGER = logging.getLogger(__name__)


@click.group()
@click.option('-v', '--verbose', is_flag=True, default=False,
              help="Increase log output verbosity.")
@click.version_option(kasserver.__version__)
def cli(verbose):
    """Manage All-Inkl DNS records through the KAS server."""
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)

#get_accounts(array $parameter) 
@cli.command(name='list')

def list_command():
    """List DNS records for zone_name."""
    kas = kasserver.KasServer()
    records = kas.list_account()
    


@cli.command()
@click.argument('fqdn')
@click.argument('record_type')
@click.argument('value')
@click.option('--ttl', default='0', help="the TTL value")
def add(fqdn, record_type, value, ttl):
    """Add a DNS record for fqdn with record_type and value."""
    LOGGER.info("Setting DNS %s record for domain %s to %s (TTL: %s)",
                record_type, fqdn, value, ttl)
    kas = kasserver.KasServer()
    kas.add_dns_record(fqdn, record_type, value, ttl)


@cli.command()
@click.argument('fqdn')
@click.argument('record_type')
def remove(fqdn, record_type):
    """Remove a DNS record for fqdn and record_type."""
    LOGGER.info("Removing DNS %s record for domain %s", record_type, fqdn)
    kas = kasserver.KasServer()
    kas.delete_dns_record(fqdn, record_type)

#@click.argument('max_account')
#@click.argument('max_domain')
#@click.argument('max_subdomain')
#@click.argument('max_webspace')
#@click.argument('max_mail_account')
#@click.argument('max_mail_forward')
#@click.argument('max_mailinglist')
#@click.argument('max_database')
#@click.argument('max_ftpuser')

@cli.command()
@click.argument('account_kas_password')
@click.argument('account_ftp_password')
@click.argument('hostname_art')
@click.argument('hostname_part1')
@click.argument('hostname_part2')
def add_subaccount(account_kas_password, account_ftp_password,hostname_art  , hostname_part1, hostname_part2):
    """Remove a DNS record for fqdn and record_type."""
 
    kas = kasserver.KasServer()
    kas.add_subaccount(account_kas_password, account_ftp_password, hostname_art, hostname_part1, hostname_part2)
