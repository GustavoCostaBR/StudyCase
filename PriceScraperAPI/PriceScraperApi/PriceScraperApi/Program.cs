using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.OpenApi.Models;
using PriceScraperApi.Services;
using PriceScraperApi.Repositories;
using PriceScraperApi.Models;
using MongoDB.Driver;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers(); // Required for API controllers
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo { Title = "PriceScraperApi", Version = "v1" });
});

// Configure MongoDB
builder.Services.AddSingleton<IMongoClient>(s =>
{
    IConfiguration configuration = s.GetRequiredService<IConfiguration>();
    var connectionString = configuration.GetSection("MongoDB:ConnectionString").Value;
    return new MongoClient(connectionString);
});

builder.Services.AddSingleton<IMongoDatabase>(s =>
{
    var client = s.GetRequiredService<IMongoClient>();
    IConfiguration configuration = s.GetRequiredService<IConfiguration>();
    string databaseName = configuration.GetSection("MongoDB:DatabaseName").Value;
    return client.GetDatabase(databaseName);
});

// Register dependencies
builder.Services.AddScoped<IProductRepository, ProductRepository>();
builder.Services.AddScoped<IProductService, ProductService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage(); // Show detailed error pages in Development
    app.UseSwagger();
    app.UseSwaggerUI(c => c.SwaggerEndpoint("/swagger/v1/swagger.json", "PriceScraperApi v1"));
}
else
{
    app.UseExceptionHandler("/Error"); // Handle exceptions in Production
    app.UseHsts(); // Use HSTS for secure connections in Production
}

app.UseHttpsRedirection();
app.UseStaticFiles();  // Enable serving static files
app.UseRouting();      // Enable routing

app.UseAuthorization(); // Enable authorization if you have authentication

app.MapControllers();   // Enable Controller endpoints.

app.Run();