from collections import defaultdict


def filter_metrics(metrics_by_month: defaultdict(list), stop_authors = [], take = 10) -> defaultdict(bool):
  potential_filter = defaultdict(lambda: False)

  for key in metrics_by_month.keys():
    authors = (
        record[0]
        for record
        in sorted(metrics_by_month[key], key = lambda x: x[1], reverse = True)
        if record[0] not in stop_authors
    )

    for i, author in enumerate(authors):
      potential_filter[author] = True

      if (i + 1) == take:
        break

  return potential_filter
