import sys, logging

def parse_reroute_rules(reroute_rules):
    reroutes = {}

    for rule in reroute_rules:
        try:
            fragments = rule.split(":=")

            source = fragments[0]
            recipient = fragments[1]

            reroutes[source] = recipient
        except Exception as e:
            logging.error("Couldn't parse reroute rules: {}".format(e))

            sys.exit(2)

    return reroutes