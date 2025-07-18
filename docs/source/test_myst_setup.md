# Test MyST and Sphinx Design Setup

This is a test file to verify that MyST parser and sphinx_design are working correctly.

## MyST Features Test

### Basic Markdown
This is regular markdown text with **bold** and *italic* formatting.

### Code Blocks
```python
def hello_world():
    print("Hello, World!")
```

### Task Lists
- [x] Install MyST parser
- [x] Install sphinx_design
- [ ] Test the setup

### Admonitions
```{note}
This is a MyST admonition using the note directive.
```

```{warning}
This is a warning admonition.
```

## Sphinx Design Features Test

### Cards
````{card}
Card Title
^^^
Card content goes here. This tests the sphinx_design extension.
````

### Tabs
````{tab-set}
```{tab-item} First Tab
Content of the first tab.
```

```{tab-item} Second Tab
Content of the second tab.
```
````

### Buttons
```{button-ref} index
:color: primary
:class: sd-rounded-pill

Go to Home
```

### Grids
````{grid} 2
```{grid-item-card} Card 1
Content of card 1
```

```{grid-item-card} Card 2
Content of card 2
```
````

## Links and References

This is a link to the [main index](index.rst).

## Math (if enabled)
$E = mc^2$

## Definition Lists

Term 1
: Definition of term 1

Term 2
: Definition of term 2

---

If you can see this file properly rendered with all the above features working, then MyST parser and sphinx_design are successfully set up!