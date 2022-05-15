import React from 'react';

import { FiltersWrapper, Orderings, CurrencyFilters, CurrencyButton } from '../styles/ComponentStyles';

const CurrencyFilter = (props) => {
  return (
    <>
      <FiltersWrapper>
        <Orderings>
          <select onChange={event => props.setFilter(event.currentTarget.value)}>
            <option value='-date' onChange={_ => props.setFilter('-date')}>Sort by Date descending (default)</option>
            <option value='date' onChange={_ => props.setFilter('date')}>Sort by Date ascending</option>
            <option value='-amount_in_huf' onChange={_ => props.setFilter('-amount_in_huf')}>Sort by Amount descending</option>
            <option value='amount_in_huf' onChange={_ => props.setFilter('amount_in_huf')}>Sort by Amount ascending</option>
          </select>
        </Orderings>
        <CurrencyFilters>
          <li onClick={_ => props.setFilter('')}>
            <CurrencyButton
              name=''
            >
              ALL
            </CurrencyButton>
          </li>
          <li onClick={_ => props.setFilter('HUF')}>
            <CurrencyButton
              name='HUF'
            >
              HUF
            </CurrencyButton>
          </li>
          <li onClick={_ => props.setFilter('USD')}>
            <CurrencyButton
              name='USD'
            >
              USD
            </CurrencyButton>
          </li>
        </CurrencyFilters>
      </FiltersWrapper>
    </>
  );
}

export default CurrencyFilter;
