## `pl-calculator` element

The `pl-calculator` element provides a web-based calculator with button and keyboard input support.

### Usage

    ```html
    <pl-question-panel>
      <pl-calculator calculator-name="example"></pl-calculator>
    </pl-question-panel>
    ```

### Customizations

| Attribute         | Type   | Default       | Description                                                                                                                                                                                                                                                 |
| ----------------- | ------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `calculator-name` | string | pl-calculator | Specifies a unique name for the calculator. The name will be used to store the calculation history for the calculator. Note that this attribute has to be unique within a question, i.e., no value for this attribute should be repeated within a question. |

### Keyboard input and shortcut

In addition to button inputs, the calculator supports keyboard input. Inputs and shortcuts follow the style of most calculators in use. e.g. The keyboard input for $a^b$ is a^b. The keyboard input for
$\sqrt{}$ is sqrt.

### Symbolic and numeric mode

The symbolic and numeric switch is mainly for symbolic variables such as $\pi$ and $e$, and fractions. In symbolic
mode, the symbols stay in their symbolic form. In numeric mode, the calculator uses the value
of the symbols to calculate the answer.

### Degree and radian mode

The calculator supports the interpretation of trigonometry functions as either degree or radian. In radian mode, any use of angle will be added a degree symbol implicitly. For example,

- In radian mode, the calculation $\sin(\frac{\pi}{2})$ gives 1, and $\sin^{-1}(1)$ gives $\frac{\pi}{2}$;
- In degree mode, the calculation $\sin(90)$ gives 1, and $\sin^{-1}(1)$ gives 90.
