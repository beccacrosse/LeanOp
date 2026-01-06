import { View, Text, StyleSheet } from 'react-native';
import * as React from 'react';
import { DataTable } from 'react-native-paper';

export default function Overview() {
  const seats = 100;
  const software_cost = 1000;
  const monthly_cost = 1000;
  const utilization = 0.75;
  const savings = 1000;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Spending Overview</Text>
      <Text style={styles.textPrimary}>
        This is a summary of your spending and utilization.
      </Text>
      <DataTable>
        <DataTable.Header>Spending & Utilization Overview</DataTable.Header>
        <DataTable.Row>
          <DataTable.Cell>Software Cost</DataTable.Cell>
          <DataTable.Cell>${software_cost}</DataTable.Cell>
        </DataTable.Row>
        <DataTable.Row>
          <DataTable.Cell>Utilization</DataTable.Cell>
          <DataTable.Cell>{utilization * 100}%</DataTable.Cell>
        </DataTable.Row>
        <DataTable.Row>
          <DataTable.Cell>Savings</DataTable.Cell>
          <DataTable.Cell>${savings}</DataTable.Cell>
        </DataTable.Row>
      </DataTable>
      <Text style={styles.textPrimary}>
        You are currently spending ${software_cost} per month on software.
      </Text>
      <Text style={styles.textPrimary}>
        You are currently utilizing {utilization * 100}% of your seats.
      </Text>
      <View style={styles.savingsContainer}>
        <Text style={styles.textPrimary}>
          You are currently saving ${savings} per month by reducing your seats.
        </Text>
      </View>
      
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#1a1a2e',
  },
  textPrimary: {
    fontSize: 16,
    marginBottom: 12,
    textAlign: 'center',
    color: '#333',
  },
  textSecondary: {
    fontSize: 14,
    marginBottom: 10,
    color: '#666',
  },
  savingsContainer: {
    backgroundColor: '#e0e0e0',
    padding: 10,
    borderRadius: 5,
    marginBottom: 20,
  },
});
