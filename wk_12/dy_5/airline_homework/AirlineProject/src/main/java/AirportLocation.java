public enum AirportLocation {
    EDI("EDI", "Edinburgh", "United Kingdom", 55.9508, -3.3615, "Europe"),
    JFK("JFK", "John F. Kennedy", "United States", 40.6442, -73.7822, "North America"),
    CDG("CDG", "Charles de Gaulle", "France", 49.0097, 2.5479, "Europe"),
    DXB("DXB", "Dubai International", "United Arab Emirates", 25.2528, 55.3644, "Asia"),
    HKG("HKG", "Hong Kong International", "Hong Kong", 22.3080, 113.9185, "Asia"),
    SYD("SYD", "Sydney Kingsford-Smith", "Australia", -33.9461, 151.1772, "Australia/Oceania"),
    BKK("BKK", "Suvarnabhumi", "Thailand", 13.6815, 100.7474, "Asia"),
    GRU("GRU", "São Paulo-Guarulhos", "Brazil", -23.4346, -46.4682, "South America"),
    NRT("NRT", "Narita International", "Japan", 35.7638, 140.3864, "Asia"),
    DUB("DUB", "Dublin", "Ireland", 53.4214, -6.2701, "Europe");

    private final String shortCode;
    private final String fullName;
    private final String country;
    private final double latitude;
    private final double longitude;
    private final String continent;

    AirportLocation(String shortCode, String fullName, String country, double latitude, double longitude, String continent) {
        this.shortCode = shortCode;
        this.fullName = fullName;
        this.country = country;
        this.latitude = latitude;
        this.longitude = longitude;
        this.continent = continent;
    }

    public String getShortCode() {
        return shortCode;
    }

    public String getFullName() {
        return fullName;
    }

    public String getCountry() {
        return country;
    }

    public double getLatitude() {
        return latitude;
    }

    public double getLongitude() {
        return longitude;
    }

    public String getContinent() {
        return continent;
    }
}

