![logo](../logo.png=250x)

# PyCUST

PyCUST is the Python actor implementation of the LOCUST-GPU code, written by Rob Akers.

This package presents a duck-typed Python actor, similar to what is produced with FC2K - but implemented from scratch to avoid headaches with continuous recompilation.

> Got any burning questions? Want to feedback? Please raise an issue here on [JIRA](https://jira.iter.org/), or email me at samuel.ward@iter.org!

## Usage

```python
from PyCUST.locust import actor as locust
locust(IDSs,"settings_locust.xml")
```

## Settings


| -DIMAS_FLAG       | Default Value            | Function                                        |
|-------------------|--------------------------|-------------------------------------------------|
| SHOT_IN           | 1                        | Shot number to read from                        |
| SHOT_OUT          | SHOT_IN                  | Shot number to write to                         |
| RUN_IN            | 1                        | Run number to read from                         |
| RUN_OUT           | RUN_IN                   | Run number to write to                          |
| USER_IN           | call getenv('USER',USER) | Whose environment to read from                  |
| USER_OUT          | USER_IN                  | Whose environment to write to                   |
| MACHINE_IN        | 'iter'                   | Machine name to read from                       |
| MACHINE_OUT       | MACHINE_IN               | Machine name to write to                        |
| ANSYS             | Do not convert           | Uses ANSYS mesh (+ dumps to input IDS)          |
|                   |                          |                                                 |

## Notes Devs

* General
    * GGD mesh currently causes segfaults, development of this part of the code has paused (dump_mesh_imas tested fine, read_mesh_imas untested)

* pload_imas.f90
    * always assumes PCYC functionality

* host_mod.f90
    * dump_mesh_imas
        * assumes empty tet space is contiguous in mesh array
        * always places vacuum component last in ids grid_subset