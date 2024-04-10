"""Command line tools for the iBridges library."""
import argparse
import sys
from pathlib import Path
from typing import Union

from ibridges.data_operations import download, upload
from ibridges.interactive import interactive_auth
from ibridges.path import IrodsPath
from ibridges.session import Session
from ibridges.sync import sync_data

try:  # Python < 3.10 (backport)
    from importlib_metadata import version
except ImportError:
    from importlib.metadata import version  # type: ignore [assignment]

MAIN_HELP_MESSAGE = f"""
iBridges CLI version {version("ibridges")}

Usage: ibridges [subcommand] [options]

Available subcommands:
    download:
        Download a data object or collection from the iRods server.
    upload:
        Upload a file or directory to the iRods server
        (which converts it to a data object/collection respectively).
    init:
        Generate json schema from distribution providers.

WARNING: For the best results it is recommended to use the Python API.

Example usage:

ibridges download "remote:~/test.txt"
ibridges upload ~/test.txt
ibridges init
ibridges sync ~/collection "remote:~/collection"

Program information:
    -v, --version - display CLI version and exit
    -h, --help    - display this help file and exit
"""


def main() -> None:
    """CLI pointing to different entrypoints."""
    # show help by default, else consume first argument
    subcommand = "--help" if len(sys.argv) < 2 else sys.argv.pop(1)

    if subcommand in ["-h", "--help"]:
        print(MAIN_HELP_MESSAGE)
    elif subcommand in ["-v", "--version"]:
        print(f"Metasyn CLI version {version('metasyn')}")

    # find the subcommand in this module and run it!
    elif subcommand == "download":
        ibridges_download()
    elif subcommand == "upload":
        ibridges_upload()
    elif subcommand == "sync":
        ibridges_sync()
    elif subcommand == "init":
        ibridges_init()
    else:
        print(f"Invalid subcommand ({subcommand}). For help see ibridges --help")
        sys.exit(1)


def ibridges_init():
    """Create a cached password for future use."""
    parser = argparse.ArgumentParser(
        prog="ibridges init",
        description="Cache your iRods password to be used later."
    )
    parser.add_argument(
        "--irods_env_path", "-p",
        help="The path to your iRods environment JSON file.",
        type=Path,
        default=None,
        required=False,
    )
    args, _ = parser.parse_known_args()
    with interactive_auth(args.irods_env_path) as session:
        assert isinstance(session, Session)
    print("ibridges init was succesful.")


def _convert_path(remote_or_local: Union[str, Path]) -> Union[Path, str]:
    if isinstance(remote_or_local, Path):
        return remote_or_local
    if remote_or_local.startswith("remote:"):
        return remote_or_local[7:]
    return Path(remote_or_local)


def _parse_local(local_path: Union[None, str, Path]) -> Path:
    if local_path is None:
        return Path.cwd()
    if isinstance(local_path, str):
        if local_path.startswith("remote:"):
            raise ValueError("Please provide a local path (not starting with 'remote:')")
        local_path = Path(local_path)
    return local_path

def _parse_remote(remote_path: Union[None, str], session: Session) -> IrodsPath:
    if remote_path is None:
        return IrodsPath(session, session.irods_home)
    if not remote_path.startswith("remote:"):
        raise ValueError("Please provide a remote path starting with 'remote:'")
    return IrodsPath(session, remote_path[7:])

def ibridges_download():
    """Download a remote data object or collection."""
    parser = argparse.ArgumentParser(
        prog="ibridges download",
        description="Download a data object or collection from an iRods server."
    )
    parser.add_argument(
        "remote_path",
        help="Path to remote iRods location starting with 'remote:'",
        type=str,
    )
    parser.add_argument(
        "local_path",
        help="Local path to download the data object/collection to.",
        type=Path,
        nargs="?",
    )
    parser.add_argument(
        "--overwrite",
        help="Overwrite the local file(s) if it exists.",
        action="store_true",
    )
    args, _ = parser.parse_known_args()
    with interactive_auth() as session:
        download(session,
                 _parse_remote(args.remote_path, session),
                 _parse_local(args.local_path),
                 overwrite=args.overwrite,
        )


def ibridges_upload():
    """Upload a local file or directory to the irods server."""
    parser = argparse.ArgumentParser(
        prog="ibridges upload",
        description="Upload a data object or collection from an iRods server."
    )
    parser.add_argument(
        "local_path",
        help="Local path to upload the data object/collection from.",
        type=Path,
    )
    parser.add_argument(
        "remote_path",
        help="Path to remote iRods location starting with 'remote:'",
        type=str,
    )
    parser.add_argument(
        "--overwrite",
        help="Overwrite the remote file(s) if it exists.",
        action="store_true",
    )
    args, _ = parser.parse_known_args()

    with interactive_auth() as session:
        upload(session,
               _parse_local(args.local_path),
               _parse_remote(args.remote_path, session),
               overwrite=args.overwrite
        )


def _parse_str(remote_or_local: str, session) -> Union[str, IrodsPath]:
    if remote_or_local.startswith("remote:"):
        return IrodsPath(session, remote_or_local[7:])
    return remote_or_local

def ibridges_sync():
    """Synchronize files/directories between local and remote."""
    parser = argparse.ArgumentParser(
        prog="ibridges sync",
        description="Synchronize files/directories between local and remote."
    )
    parser.add_argument(
        "source",
        help="Source path to synchronize from.",
        type=str,
    )
    parser.add_argument(
        "destination",
        help="Destination path to synchronize to.",
        type=str,
    )
    parser.add_argument(
        "--dry-run",
        help="Do not perform the synchronization, but list the files to be updated.",
        action="store_true"
    )
    args, _ = parser.parse_known_args()


    with interactive_auth() as session:
        sync_data(session,
                  _parse_str(args.source, session),
                  _parse_str(args.destination, session),
                  dry_run=args.dry_run,
        )
