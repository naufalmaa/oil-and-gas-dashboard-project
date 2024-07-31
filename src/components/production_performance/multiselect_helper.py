def to_multiselect_options(values: list[str]) -> list[dict[str, str]]:
    return [{"label": value, "value": value} for value in values]

