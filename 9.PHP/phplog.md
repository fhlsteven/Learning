# 记录

## `<?php if ($this->credit_token): ?> readonly value="<?= $this->credit_token ?>" <?php endif; ?> />` 中的 `->` 和 `<?= $this->credit_token ?>` 如何解释

1. `->` 用于访问对象的属性或调用对象的方法。

2. `<?= $this->credit_token ?>`  是一种简写形式的 PHP 语法，也称为短标签或短输出标签。它用于在 HTML 中嵌入 PHP 变量的值。这个语法的作用与 `<?php echo $credit_token; ?>` 相同。
