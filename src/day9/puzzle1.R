library(tidyverse)

path <- normalizePath(file.path("inputs", "day9", "puzzle1.txt"))
lines <- readr::read_lines(path)

height_data <- lines %>%
  map(str_split, pattern="", n=100) %>%
  bind_cols() %>%
  unnest(everything()) %>%
  set_names(1:100) %>%
  mutate(
    x = row_number()
  ) %>%
  pivot_longer(`1`:`100`, names_to = "y", values_to = "height") %>%
  mutate(across(where(is.character), as.integer)) %>%
  mutate(
    l_x = x - 1,
    l_y = y,
    r_x = x + 1,
    r_y = y,
    d_x = x,
    d_y = y - 1,
    u_x = x,
    u_y = y + 1
  )

adjacent_data <- height_data %>%
  left_join(height_data %>% select(x, y, height), by=c(l_x="x", l_y="y"), suffix=c("", "_l")) %>%
  left_join(height_data %>% select(x, y, height), by=c(r_x="x", r_y="y"), suffix=c("", "_r")) %>%
  left_join(height_data %>% select(x, y, height), by=c(u_x="x", u_y="y"), suffix=c("", "_u")) %>%
  left_join(height_data %>% select(x, y, height), by=c(d_x="x", d_y="y"), suffix=c("", "_d")) %>%
  mutate(
    across(starts_with("height_"), ~replace_na(.x > height, TRUE), .names="{.col}_lower")
  ) %>%
  mutate(
    all_lower = reduce(select(., ends_with("_lower")), `&`)
  )

part_one <- adjacent_data %>%
  filter(all_lower) %>%
  mutate(
    risk_level = height + 1
  ) %>%
  summarise(risk_level_sum = sum(risk_level))

print(part_one)

