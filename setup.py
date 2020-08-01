from setuptools import setup
import pathlib

root = pathlib.Path(__file__).parent

setup(name="automute",
      version="1.0.0",
      description="Automatically mutes.",
      long_description=(root / "README.md").read_text("utf-8"),
      author="SpookyBear0",
      author_email="collinmcarroll@gmail.com",
      packages=["automute"],
      zip_safe=False,
)
