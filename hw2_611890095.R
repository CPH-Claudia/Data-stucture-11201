rm(list = ls(all = TRUE))
graphics.off()

# 定義二元樹節點
# install.packages("R6")
library(R6)
Node <- R6Class("Node",
                public = list(
                  value = NULL,
                  left = NULL,
                  right = NULL,
                  initialize = function(value) {
                    self$value <- value
                  }
                )
)

# 將中序運算式轉換為二元樹
build_expression_tree <- function(expression) {
  precedence <- list(`+` = 1, `-` = 1, `*` = 2, `/` = 2)
  is_operator <- function(op) op %in% names(precedence)
  
  build_tree_from_infix <- function(exp) {
    stack <- list()
    for (char in strsplit(exp, "")[[1]]) {
      if (grepl("[0-9]", char)) {
        node <- Node$new(char)
        stack <- c(stack, list(node))
      } else if (is_operator(char)) {
        node <- Node$new(char)
        if (length(stack) >= 2) {
          node$right <- stack[[length(stack)]]
          node$left <- stack[[length(stack) - 1]]
          stack <- stack[-(length(stack) - 1):length(stack)]
          stack <- c(stack, list(node))
        } else {
          # Handle error or incomplete expression here
          print("Incomplete expression")
          return(NULL)
        }
      }
    }
    root <- stack[[1]]
    return(root)
  }
  
  return(build_tree_from_infix(expression))
}

# 產生後序運算式
postfix_expression <- function(root) {
  if (!is.null(root)) {
    left <- postfix_expression(root$left)
    right <- postfix_expression(root$right)
    return(paste(left, right, root$value, sep = ""))
  }
  return("")
}

# 計算後序運算式結果
evaluate_postfix_expression <- function(postfix) {
  stack <- list()
  operators <- c("+", "-", "*", "/")
  
  for (char in strsplit(postfix, "")[[1]]) {
    if (grepl("[0-9]", char)) {
      stack <- c(stack, as.numeric(char))
    } else if (char %in% operators) {
      operand2 <- stack[[length(stack)]]
      operand1 <- stack[[length(stack) - 1]]
      stack <- stack[-(length(stack) - 1):length(stack)]
      if (char == "+") {
        stack <- c(stack, operand1 + operand2)
      } else if (char == "-") {
        stack <- c(stack, operand1 - operand2)
      } else if (char == "*") {
        stack <- c(stack, operand1 * operand2)
      } else if (char == "/") {
        stack <- c(stack, operand1 / operand2)
      }
    }
  }
  return(stack[[1]])
}

# 測試程式碼
infix_expression <- "2*(8+7)-9/3"
root <- build_expression_tree(infix_expression)
postfix <- postfix_expression(root)
cat(paste("後序運算式(Postfix): ", postfix, "\n"))
result <- evaluate_postfix_expression(postfix)
cat(paste("計算結果: ", result, "\n"))