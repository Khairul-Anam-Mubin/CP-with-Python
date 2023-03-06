using RentAdvertisementSystem.Database;

namespace RentAdvertisementSystem.Models
{
    public class RentItem : IRepositoryItem
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public string Type { get; set; }
        public string Description { get; set; }
        public double Value { get; set; }
        public string Location { get; set; }
        public DateTime PostedAt { get; set; }
        public string FilePath { get; set; }
        public string UserId { get; set; }
        public RentItem()
        {
            Id = Guid.NewGuid().ToString();
        }
    }
}