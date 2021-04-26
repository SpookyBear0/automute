from setuptools import setup
import pathlib

root = pathlib.Path(__file__).parent

setup(name="autodeafen",
      version="1.0.0",
      description="Automatically defeans discord when far in gd.",
      long_description=(root / "README.md").read_text("utf-8"),
      author="SpookyBear0",
      zip_safe=False,
)
