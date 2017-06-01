#!/usr/bin/env python
from distutils.core import setup

setup(name='revolve',
      version=0.2,
      description='Revolve: robot evolution framework',
      author='Elte Hupkes',
      author_email='elte@hupkes.org',
      url='https://github.com/ElteHupkes/revolve',
      packages=['revolve',
                'revolve.gazebo',
                'revolve.gazebo.manage',
                'revolve.build',
                'revolve.build.sdf',
                'revolve.build.sdf.body',
                'revolve.build.sdf.neural_net',
                'revolve.convert',
                'revolve.generate',
                'revolve.spec',
                'revolve.spec.msgs',
                'revolve.angle',
                'revolve.angle.manage',
                'revolve.angle.robogen',
                'revolve.angle.robogen.spec',
                'revolve.angle.robogen.body_parts',
                'revolve.util',
                'revolve.util.supervisor',
                'revolve.logging'],
      install_requires=['PyYAML', 'pygazebo', 'protobuf', 'sdfbuilder', 'numpy', 'psutil']
      )

