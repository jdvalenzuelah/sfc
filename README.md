# Server Fan Control

Dependency free framework for a fan control loop using python. This framework provides a ControlLoop class in charge of executing a control loop algorithm.

# Usage

It is composed by 3 classes:

- `ControlLoop` executes the control algorithm
- `CommunicationBuffer` works as a bridge between the control loop and the server system
- `FanSpeedCurve` Defines the adjustments to be made based on the feedback obtained from the server system

The `CommunicationBuffer` and `FanSpeedCurve` are abstract classes and a implementation must be passed to `ControlLoop`


Given implementations:
```python
class Server(CommunicationBuffer):
    ...

class Control(FanSpeedCurve):
    ...
```

The `ControlLoop` is used like:
```python
if __name__ == '__main__':
    server = Server()
    control = Control()

    control = ControlLoop(server, control)

    control.start()

```