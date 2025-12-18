import { View, Text, StyleSheet } from 'react-native';

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
      <Text style={styles.textPrimary}>
        You are currently spending ${software_cost} per month on software.
      </Text>
      <Text style={styles.textPrimary}>
        You are currently utilizing {utilization * 100}% of your seats.
      </Text>
      <Text style={styles.textPrimary}>
        You are currently saving ${savings} per month by reducing your seats.
      </Text>
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
});
