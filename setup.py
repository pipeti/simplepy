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
            'pytz==2018.4',
            'kafka-python==1.3.3',
            'click==6.6',
            'Werkzeug==0.11.11',
            'itsdangerous==0.24',
            'functools32==3.2.3-2',
            'jsonschema==2.6.0',
            'markupsafe==1.0',
            'jinja2==2.8.1',
            'flask==0.12.1',
            'meld3==1.0.2',
            'supervisor==3.2.3',
            'psycopg2==2.7.3.2',
            'gunicorn==19.7.1'
      ]
      zip_safe=False)
