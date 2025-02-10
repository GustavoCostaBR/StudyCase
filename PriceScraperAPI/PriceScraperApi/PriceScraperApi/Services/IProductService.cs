using PriceScraperApi.Models;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace PriceScraperApi.Services
{
    public interface IProductService
    {
        Task<Product> GetProduct(string id);
        Task<IEnumerable<Product>> GetAllProducts();
        Task CreateProduct(Product product);
    }
}