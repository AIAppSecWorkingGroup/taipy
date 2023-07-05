# Copyright 2023 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import pathlib
import sys

from cookiecutter.main import cookiecutter

from taipy._cli._base_cli import _CLI
from taipy.logger._taipy_logger import _TaipyLogger


class _ScaffoldCLI:
    __logger = _TaipyLogger._get_logger()
    __TAIPY_PATH = pathlib.Path(__file__).parent.parent.resolve() / "templates"

    _TEMPLATE_MAP = {str(x.name): str(x) for x in __TAIPY_PATH.iterdir() if x.is_dir()}

    @classmethod
    def create_parser(cls):
        create_parser = _CLI._add_subparser("create", help="Create a new Taipy application.")
        create_parser.add_argument(
            "--template",
            choices=list(cls._TEMPLATE_MAP.keys()),
            default="taipy-default-template",
            help="The Taipy template to create new application.",
        )

    @classmethod
    def parse_arguments(cls):
        args = _CLI._parse()

        if getattr(args, "which", None) == "create":
            application_path = cookiecutter(cls._TEMPLATE_MAP[args.template])
            cls.__logger.info(f"Taipy application created at {application_path}")
            sys.exit(0)
