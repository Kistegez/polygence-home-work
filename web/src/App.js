import React, { useState } from 'react';
import Form from './components/Form';
import FiltersAndOrderings from './components/FiltersAndOrderings';
import SpendingList from './components/SpendingList';
import Layout from './components/Layout';

export default function App() {
  const [spendings, setSpendings] = useState([]);
  let [filter, setFilter] = useState(null);

  return (
    <>
      <Layout>
        <Form />
        <FiltersAndOrderings setFilter={setFilter}/>
        <SpendingList
          spendings={spendings}
          setSpendings={setSpendings}
          filter={filter}
        />
      </Layout>
    </>
  );
}
