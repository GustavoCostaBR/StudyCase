using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace PriceScraperApi.Models;

public class Product
{
    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string? Id { get; private set; }

    [BsonElement("Name")]
    public string Name { get; set; } = string.Empty; // Added default value

    [BsonElement("Price")]
    public decimal Price { get; set; }

    [BsonElement("PricePerKg")]
    public decimal PricePerKg { get; set; }

    [BsonElement("OfferPrice")]
    public decimal OfferPrice { get; set; }

    [BsonElement("OfferPriceClubCard")]
    public decimal OfferPriceClubCard { get; set; }

    [BsonElement("Url")]
    public string Url { get; set; } = string.Empty; // Added default value

    [BsonElement("DateOfOffer")]
    public DateTime DateOfOffer { get; set; }

    [BsonElement("DateOfOfferClubCard")]
    public DateTime DateOfOfferClubCard { get; set; }

    [BsonElement("Timestamp")]
    public DateTime Timestamp { get; set; } = DateTime.UtcNow;
}