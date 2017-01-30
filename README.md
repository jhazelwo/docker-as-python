# docker-as-python

* Don't use this! Writing this just for fun.

```python
import docker

image = docker.Docker('owner/project:0.0', './test-Dockerfile')

image.build_rm = True
image.build()
print(image.last_command)
print(image.build_log)

image.run_rm = True
image.tty = True
image.interactive = True
image.entrypoint = '/bin/echo'
image.extra_args = 'hello world'
image.run()
```
