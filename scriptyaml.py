import openai
import yaml


# Set your OpenAI API key
openai.api_key = "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"

def generate_response(prompt):
    # Call the OpenAI API to generate a response based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the language model
        prompt=prompt,
        max_tokens=100  # Adjust as needed
    )
    return response.choices[0].text.strip()


# Your YAML configuration
yaml_config = """
apiVersion: v1
kind: Service
metadata:
  name: wordpress
  labels:
    app: wordpress
spec:
  ports:
    - port: 80
  selector:
    app: wordpress
    tier: frontend
  type: LoadBalancer
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: wp-pv-claim
  labels:
    app: wordpress
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
  labels:
    app: wordpress
spec:
  selector:
    matchLabels:
      app: wordpress
      tier: frontend
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
        tier: frontend
    spec:
      containers:
      - image: wordpress:6.2.1-apache
        name: wordpress
        env:
        - name: WORDPRESS_DB_HOST
          value: wordpress-mysql
        - name: WORDPRESS_DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        - name: WORDPRESS_DB_USER
          value: wordpress
        ports:
        - containerPort: 80
          name: wordpress
        volumeMounts:
        - name: wordpress-persistent-storage
          mountPath: /var/www/html
      volumes:
      - name: wordpress-persistent-storage
        persistentVolumeClaim:
          claimName: wp-pv-claim

"""

# Add a prompt indicating the intention to scale up the application
prompt = f"Scale up the application based on the following YAML configuration:\n{yaml_config}"

response = generate_response(prompt)
print(response)