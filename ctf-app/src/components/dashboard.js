import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

import './css/dashboard.css';

const Dashboard = () => {
  const navigate = useNavigate();
  const [items, setItems] = useState([]);

  const config = {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`,
    }
  };

  useEffect(() => {
    const fetchItems = async () => {
      const response = await axios.get('http://localhost:5000/api/items', config);
      setItems(response.data.items);
    };
    fetchItems();
  }, []);

  const handleItemClick = (item) => {
    axios.get(`http://localhost:5000/api/items/${item}`, config)
      .then(response => {
        console.log(response.data);
        if (item === 'F' && !response.data.is_admin) {
          alert("You don't have access to this item!");
        } else {
          navigate(`/item/${item}`);
        }
      })
      .catch(error => {
        console.log(error);
        alert('Error fetching item details!');
      });
  };

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      <div className="item-list">
        {items.map((item) => (
          <div
            className="item"
            key={item}
            onClick={() => handleItemClick(item)}
          >
            {item}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
