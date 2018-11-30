from setuptools import setup

setup(name='simplepy',
      version='0.1',
      description='Simple-pie!!!',
      url='http://github.com/pipeti/simplepy',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['simplepy'],
      install_requires=[
            'psycopg2>=2.7.3.2',
            'pytz>=2018.4',
            'gunicorn>=19.7.1',
            'jsonschema>=2.5',
            'Flask>=0.12.1',
            'kafka-python>=1.3.3'
      ]
      zip_safe=False)
