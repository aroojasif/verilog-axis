#!/usr/bin/env python3

# Copyright 2023 Nico De Simone.

from pathlib import Path
from tsfpga.module import BaseModule
from tsfpga.hdl_file import HdlFile
import verilog_axis

class Module(BaseModule):
    def __init__(self):
        print("DEBUG __file__:", __file__)
        print("DEBUG verilog_axis.__file__:", verilog_axis.__file__)
        super().__init__(
            path=Path(verilog_axis.__file__).parent.parent.resolve(),
            library_name="verilog_axis",
        )

    def get_synthesis_files(self, **kwargs):
        folders = [self.path / "rtl"]
        return [
            HdlFile(file_path)
            for file_path in self._get_file_list(
                folders=folders, file_endings=(".vhd", ".vhdl", ".v")
            )
        ]

    def get_simulation_files(self, **kwargs):
        folders = [self.path / "rtl", self.path.parent / "test"]
        return [
            HdlFile(file_path)
            for file_path in self._get_file_list(
                folders=folders, file_endings=(".vhd", ".vhdl", ".v")
            )
        ]

if __name__ == "__main__":
    m = Module()

    print("Synthesis files:")
    for f in m.get_synthesis_files():
        print(" →", f.path)

    print("Simulation files:")
    for f in m.get_simulation_files():
        print(" →", f.path)
