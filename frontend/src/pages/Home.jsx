import React from 'react';
import { Box, Typography, Button } from '@mui/material';

const Home = () => {
  console.log('Home component is being rendered');
  return (
    <Box mt={5} textAlign="center">
      <Typography variant="h3">Welcome to Tax Filing Portal</Typography>
      <img src="/images/tax-filing.jpg" alt="Tax Filing" style={{ width: '100%', maxWidth: '600px', marginTop: '20px' }} />
      <Typography variant="body1" mt={2}>
        Secure, efficient, and professional tax filing services at your fingertips.
      </Typography>
      <Button variant="contained" color="primary" href="/signup" style={{ marginTop: '20px' }}>
        Get Started
      </Button>
    </Box>
  );
};

export default Home;
