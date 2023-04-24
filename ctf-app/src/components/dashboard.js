import React, { useState, useEffect } from 'react';
import axios from 'axios';

import './css/dashboard.css';

const Dashboard = () => {
  const [items, setItems] = useState([]);
  const [itemData, setItemData] = useState(null);
  const [modalVisible, setModalVisible] = useState(false);

  const config = {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`,
    }
  };

  useEffect(() => {
    const fetchItems = async () => {
      const response = await axios.get('http://localhost:5000/api/items', config);
      setItems(response.data);
    };
    fetchItems();
  }, []);

  const handleItemClick = async (item) => {
    try {
      const response = await axios.get(`http://localhost:5000/api/items/${item}`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        responseType: 'blob',
      });
      setItemData(URL.createObjectURL(response.data));
      setModalVisible(true);
    } catch (error) {
        if(error.response.status === 404){
          alert('Item not found');
        }
        else if(error.response.status === 403){
          alert('You are not authorized to view this item')
        }
      };
  };

  const closeModal = () => {
    setModalVisible(false);
    setItemData(null);
  };

  return (
    <div className="dashboard">
      <h1>Capture the .......</h1>
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
      {modalVisible && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>
              &times;
            </span>
            <img className="modal-image" src={itemData} alt="item" />
          </div>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
