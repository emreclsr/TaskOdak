def create_query(app, location):
    """
    This function create query with filtered based on app and location name.

    Parameters
    ----------
    app: String
        Alternatives: Zamit, Ronstring, Biodex, Treeflex, Regrant, Namfix, Domainer, Tree, Voyatouch
    location: String
        Alternatives: Mwaya, Tokyo, Mora, Itu, Port Antonio, Bendo, Guider, Ruuki, Guider, Setro, Jiangmen
    Returns
    -------
    String

    """

    from pypika import Query, Table

    # Table definition
    app_usage = Table("app_usage")
    apps = Table("apps")
    locations = Table("locations")
    customers = Table("customers")

    # Create query
    q = Query() \
        .from_(app_usage) \
        .join(customers) \
        .on(app_usage.customer_id == customers.id) \
        .join(apps) \
        .on(app_usage.app_id == apps.id) \
        .join(locations) \
        .on(app_usage.location_id == locations.id) \
        .select(app_usage.star) \
        .select(customers.star) \
        .select(apps.star) \
        .select(locations.star) \
        .where(apps.app_name == app) \
        .where(locations.location_name == location)

    str_q = str(q)
    str_q = str_q.replace('"', '')

    return str_q

