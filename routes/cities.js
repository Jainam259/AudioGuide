// Add a new POST endpoint to add a city
router.post('/cities', async (req, res) => {
  try {
    const { name, country, population, description } = req.body;
    
    // Validate the input
    if (!name || !country) {
      return res.status(400).json({ message: 'City name and country are required' });
    }
    
    // Save to database (example using a model)
    const newCity = await City.create({
      name,
      country,
      population: population || 0,
      description: description || ''
    });
    
    return res.status(201).json(newCity);
  } catch (error) {
    console.error('Error adding city:', error);
    return res.status(500).json({ message: 'Failed to add city' });
  }
});

// GET endpoint to retrieve all cities
router.get('/cities', async (req, res) => {
  try {
    const cities = await City.findAll();
    return res.json(cities);
  } catch (error) {
    console.error('Error fetching cities:', error);
    return res.status(500).json({ message: 'Failed to fetch cities' });
  }
}); 