import React from 'react';
import { Box, Typography } from '@mui/material';

const Dashboard = () => {
  return (
    <Box mt={5} textAlign="center">
      <Typography variant="h4">Dashboard</Typography>
      <Typography variant="body1" mt={2}>
        Welcome to your dashboard!
      </Typography>
    </Box>
  );
};

export default Dashboard;
