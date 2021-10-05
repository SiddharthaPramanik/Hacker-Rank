SELECT N, IF(
    P IS NULL, "Root",
    IF(N in (SELECT P FROM BST), "Inner", "Leaf")
)
FROM BST
ORDER BY N ASC