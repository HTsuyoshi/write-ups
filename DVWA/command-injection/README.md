# Command injection

#### Low

Testing some IPs in the forms, we can get the output of the command `ping`.

In the `Low` level there aren't any filter so we can just put `;` to end a command and start a new command.

Example:

```
; whoami
```

#### Medium

In the `Medium` level some chars aren't accepted like `;` and `||`

But we can still redirect the output using `|` or use the or operator `||`

Example:

```
| whoami
```

#### High

In the `High` level some chars aren't accepted, but there is an typo in the source code

So we can still redirect the output using `|`

Example:

```
127.0.0.1 | whoami
```
