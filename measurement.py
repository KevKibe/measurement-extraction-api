import cv2
import numpy as np
from utils import resize_image

def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Noise reduction using Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Contrast enhancement using histogram equalization
    equalized = cv2.equalizeHist(blurred)
    
    # Normalization
    normalized = cv2.normalize(equalized, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    
    return normalized

def extract_measurements(front_image, side_image, user_height):
    # Preprocess images
    front_rgb = cv2.cvtColor(cv2.imdecode(np.frombuffer(front_image.read(), np.uint8), -1), cv2.COLOR_BGR2RGB)
    side_rgb = cv2.cvtColor(cv2.imdecode(np.frombuffer(side_image.read(), np.uint8), -1), cv2.COLOR_BGR2RGB)
    
    # Resize images to a common size
    front_resized = resize_image(front_rgb, width=800)
    side_resized = resize_image(side_rgb, width=800)
    
    # Preprocess images
    front_preprocessed = preprocess_image(front_resized)
    side_preprocessed = preprocess_image(side_resized)

    # Feature extraction and measurement estimation
    height = user_height
    chest = estimate_chest(front_preprocessed)
    waist = estimate_waist(front_preprocessed)
    hip = estimate_hip(side_preprocessed)
    shoulder_width = estimate_shoulder_width(front_preprocessed)
    arm_length = estimate_arm_length(front_preprocessed)
    leg_length = estimate_leg_length(side_preprocessed)
    neck_circumference = estimate_neck_circumference(front_preprocessed)
    head_circumference = estimate_head_circumference(front_preprocessed)
    foot_length = estimate_foot_length(side_preprocessed)
    wrist_circumference = estimate_wrist_circumference(front_preprocessed)
    bicep_circumference = estimate_bicep_circumference(front_preprocessed)
    
    # Range checks and validations
    if height > 250:
        raise ValueError("Height exceeds maximum limit")
 

    measurements = {
        "height": round(height, 1),
        "chest": round(chest, 1),
        "waist": round(waist, 1),
        "hip": round(hip, 1),
        "shoulder_width": round(shoulder_width, 1),
        "arm_length": round(arm_length, 1),
        "leg_length": round(leg_length, 1),
        "neck_circumference": round(neck_circumference, 1),
        "head_circumference": round(head_circumference, 1),
        "foot_length": round(foot_length, 1),
        "wrist_circumference": round(wrist_circumference, 1),
        "bicep_circumference": round(bicep_circumference, 1)
    }
    
    return measurements, user_height

# Modify estimation functions to take preprocessed images as input
def estimate_chest(front_image):
    # Placeholder function for chest measurement estimation
    # Example: You can implement contour analysis to estimate chest circumference
    contours, _ = cv2.findContours(front_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    chest_area = 0
    for contour in contours:
        chest_area += cv2.contourArea(contour)
    chest_circumference = np.sqrt(chest_area / np.pi) * 2 * np.pi
    return chest_circumference

def estimate_waist(front_image):
    # Placeholder function for waist measurement estimation
    # Example: You can implement contour analysis to estimate waist circumference
    contours, _ = cv2.findContours(front_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    waist_area = 0
    for contour in contours:
        waist_area += cv2.contourArea(contour)
    waist_circumference = np.sqrt(waist_area / np.pi) * 2 * np.pi
    return waist_circumference

def estimate_hip(side_image):
    # Placeholder function for hip measurement estimation
    # Example: You can implement contour analysis to estimate hip circumference
    contours, _ = cv2.findContours(side_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    hip_area = 0
    for contour in contours:
        hip_area += cv2.contourArea(contour)
    hip_circumference = np.sqrt(hip_area / np.pi) * 2 * np.pi
    return hip_circumference

def estimate_shoulder_width(front_image):
    # Placeholder function for shoulder width estimation
    # Example: You can find the widest distance between shoulder contours
    contours, _ = cv2.findContours(front_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_width = 0
    for contour in contours:
        _, _, width, _ = cv2.boundingRect(contour)
        if width > max_width:
            max_width = width
    return max_width


def estimate_arm_length(front_image):
    # Placeholder function for arm length estimation
    # Example: You can find the longest contour representing the arm
    contours, _ = cv2.findContours(front_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        raise ValueError("No contours found")
    
    max_length = 0
    for contour in contours:
        if len(contour) > 0:  # Check if contour is valid
            length = cv2.arcLength(contour, True)
            if length > max_length:
                max_length = length
    return max_length



def estimate_leg_length(side_image):
    # Placeholder function for leg length estimation
    # Example: You can find the longest contour representing the leg
    contours, _ = cv2.findContours(side_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_length = 0
    for contour in contours:
        length = cv2.arcLength(contour, True)
        if length > max_length:
            max_length = length
    return max_length


def estimate_neck_circumference(front_image):
    # Placeholder function for neck circumference estimation
    # Example: You can implement contour analysis to estimate neck circumference
    contours, _ = cv2.findContours(front_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    neck_area = 0
    for contour in contours:
        neck_area += cv2.contourArea(contour)
    neck_circumference = np.sqrt(neck_area / np.pi) * 2 * np.pi
    return neck_circumference

def estimate_head_circumference(front_image):
    # Placeholder function for head circumference estimation
    # Example: You can implement contour analysis to estimate head circumference
    contours, _ = cv2.findContours(front_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    head_area = 0
    for contour in contours:
        head_area += cv2.contourArea(contour)
    head_circumference = np.sqrt(head_area / np.pi) * 2 * np.pi
    return head_circumference

def estimate_foot_length(side_image):
    # Placeholder function for foot length estimation
    # Example: You can implement contour analysis to estimate foot length
    contours, _ = cv2.findContours(side_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    foot_length = 0
    for contour in contours:
        _, _, width, height = cv2.boundingRect(contour)
        if height > foot_length:
            foot_length = height
    return foot_length

def estimate_wrist_circumference(front_image):
    # Placeholder function for wrist circumference estimation
    # Example: You can implement contour analysis to estimate wrist circumference
    contours, _ = cv2.findContours(front_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    wrist_area = 0
    for contour in contours:
        wrist_area += cv2.contourArea(contour)
    wrist_circumference = np.sqrt(wrist_area / np.pi) * 2 * np.pi
    return wrist_circumference

def estimate_bicep_circumference(front_image):
    # Placeholder function for bicep circumference estimation
    # Example: You can implement contour analysis to estimate bicep circumference
    contours, _ = cv2.findContours(front_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bicep_area = 0
    for contour in contours:
        bicep_area += cv2.contourArea(contour)
    bicep_circumference = np.sqrt(bicep_area / np.pi) * 2 * np.pi
    return bicep_circumference
