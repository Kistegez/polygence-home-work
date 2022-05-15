import React, { useState } from 'react';
import Form from './components/Form';
import FiltersAndOrderings from './components/FiltersAndOrderings';
import SpendingList from './components/SpendingList';
import Layout from './components/Layout';

export default function App() {
  const [spendings, setSpendings] = useState([]);
  const [filter, setFilter] = useState('');
  const [order, setOrder] = useState([]);

  return (
    <>
      <Layout>
        <Form />
        <FiltersAndOrderings setFilter={setFilter} setOrder={setOrder}/>
        <SpendingList
          spendings={spendings}
          setSpendings={setSpendings}
          filter={filter}
          order={order}
        />
      </Layout>
    </>
  );
}
